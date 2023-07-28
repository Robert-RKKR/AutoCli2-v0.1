# Django - models import:
from django.db import models

# Django - translation model import:
from django.utils.translation import gettext_lazy as _

# Django - internal import:
from django_celery_beat.models import IntervalSchedule
from django_celery_beat.models import PeriodicTask

# AutoCli2 - base models import:
from autocli2.base.models.identification import IdentificationModel
from autocli2.base.models.administrator import AdministratorModel

# AutoCli2 - connector model import:
from connector.models.connection_template import ConnectionTemplate

# AutoCli2 - inventory model import:
from inventory.models.host import Host

# AutoCli2 - constance's import:
from autocli2.base.constants.executor_type import ExecutorTypeChoices
from autocli2.base.constants.task import TaskChoices


# Support class:
class ExecutorConnectionTemplate(models.Model):

    class Meta:
        verbose_name = _('Executor Connection Template')
        verbose_name_plural = _('Executor Connection Templates')

    executor = models.ForeignKey(
        'Executor',
        on_delete=models.PROTECT,
    )
    connection_template = models.ForeignKey(
        ConnectionTemplate,
        on_delete=models.PROTECT,
    )
    order = models.IntegerField(
        default=0
    )

    # object representation:
    def __repr__(self) -> str:
        return f'{self.order}: {self.executor} - {self.connection_template}'

    def __str__(self) -> str:
        return  f'{self.order}: {self.executor} - {self.connection_template}'
    
    # Natural key representation:
    def natural_key(self):
        return f'{self.order}: {self.executor} - {self.connection_template}'


# Executor model class:
class Executor(IdentificationModel, AdministratorModel):

    class Meta:
        
        # Model name values:
        verbose_name = _('Executor')
        verbose_name_plural = _('Executors')

    # Relations with other classes:
    hosts = models.ManyToManyField(
        Host,
        verbose_name=_('Hosts'),
        help_text=_('Related hosts objects on witch execution will be '\
            'executed (Provides information such as host IP or domain '
            'name, platform, and credentials used to connect to the host).'),
        blank=True,
    )
    connection_templates = models.ManyToManyField(
        ConnectionTemplate,
        through=ExecutorConnectionTemplate,
        verbose_name=_('Connection templates'),
        help_text=_('Related connection template object based on which '
                    'execution will be executed (Provides information about SSH / '
                    'HTTP(S) command or URL executed on host).'),
        blank=True,
    )

    # Executor schedule:
    interval = models.ForeignKey(
        IntervalSchedule, on_delete=models.CASCADE,
        null=True, blank=True, verbose_name=_('Interval Schedule'),
        help_text=_('Interval Schedule to run the task on.  '
                    'Set only one schedule type, leave the others null.'),
    )

    def create_name(self):
        return f'Auto execute task: {self.pk}'

    def _task_schedule(self):
        if self.interval:
            # Create task name:
            name = self.create_name()
            # Update / create task scheduler:
            try: # Try to collect periodic task:
                periodic_task = PeriodicTask.objects.get(name=name)
            except: # Create periodic task if not exist:
                periodic_task = PeriodicTask.objects.create(
                    name=name, interval=self.interval)
            else: # Update periodic task interval field:
                periodic_task.interval = self.interval
            # Update task:
            periodic_task.task = 'execute_task'
            # Update task arguments:
            periodic_task.args = [self.pk]
            # Save updated periodic task object:
            periodic_task.save()

    # Model save method override:
    def save(self, *args, **kwargs):
        # Execute default save method:
        super(Executor, self).save(*args, **kwargs)
        # update / create task scheduler:
        self._task_schedule()

    # Model update override:
    def update(self, *args, **kwargs):
        # Execute default update method:
        super(Executor, self).update(*args, **kwargs)
        # update / create task scheduler:
        self._task_schedule()

    # Model delete override:
    def delete(self, *args, **kwargs):
        # Create task name:
        name = self.create_name()
        try: # Try to delete task scheduler:
            periodic_task = PeriodicTask.objects.get(name=name)
        except: # Pass if periodic task doesn't exist:
            pass
        else: # Delete if periodic task exist:
            periodic_task.delete()
        # Execute default delete method:
        super(Executor, self).delete(*args, **kwargs)
