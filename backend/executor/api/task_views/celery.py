# Celery - application import:
from autocli2.celery import app

# AutoCli2 - base view set import:
from autocli2.base.api.base_viewset import BaseListViewSet


# Celery views classes:
class CeleryReportView(BaseListViewSet):
    
    def collect_data(self):
        """
        Return human readable report for each worker.
        """
        
        try: # Try to collect Celery related data:
            celery_data = app.control.inspect().report()
        except: # Return false if the process has failed:
            celery_data = False
        finally:
            return celery_data


# Celery views classes:
class CeleryStatsView(BaseListViewSet):
    
    def collect_data(self):
        """
        Return statistics of worker.
        """

        try: # Try to collect Celery related data:
            celery_data = app.control.inspect().stats()
        except: # Return false if the process has failed:
            celery_data = False
        finally:
            return celery_data


# Celery views classes:
class CeleryRegisteredTasksView(BaseListViewSet):
    
    def collect_data(self):
        """
        Return all registered tasks per worker.
        """
        
        try: # Try to collect Celery related data:
            celery_data = app.control.inspect().registered()
        except: # Return false if the process has failed:
            celery_data = False
        finally:
            return celery_data


# Celery views classes:
class CeleryReservedView(BaseListViewSet):
    
    def collect_data(self):
        """
        Return list of currently reserved tasks, not including scheduled/active.
        """
        
        try: # Try to collect Celery related data:
            celery_data = app.control.inspect().reserved()
        except: # Return false if the process has failed:
            celery_data = False
        finally:
            return celery_data


# Celery views classes:
class CeleryRevokedView(BaseListViewSet):
    
    def collect_data(self):
        """
        Return list of revoked tasks.
        """
        
        try: # Try to collect Celery related data:
            celery_data = app.control.inspect().revoked()
        except: # Return false if the process has failed:
            celery_data = False
        finally:
            return celery_data


# Celery views classes:
class CeleryScheduledView(BaseListViewSet):
    
    def collect_data(self):
        """
        Return list of scheduled tasks with details.
        """
        
        try: # Try to collect Celery related data:
            celery_data = app.control.inspect().scheduled()
        except: # Return false if the process has failed:
            celery_data = False
        finally:
            return celery_data
