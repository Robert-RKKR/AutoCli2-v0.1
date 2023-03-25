# AutoCli2 - base models import:
from autocli2.base.models.base_model import BaseModel

# Collect object data function:
def collect_object_data(instance: BaseModel) -> dict:
    """
    Function collect object data based on provided object.

    Return: Dict
        - app_name = Name of the object application.
        - model_name = Name of the object model.
        - object_id = Correlated object PK representation.
        - object_representation = Object representation.
    """

    # Check if instance belongs or inherits from BaseModel class:
    if isinstance(instance, BaseModel):
        try: # Try to collect object representation:
            object_representation = instance.name
        except:
            object_representation = 'Empty'
        finally:
            try: # Try to collect object related information:
                application_name = instance.__class__._meta.app_label
                model_name = instance.__class__.__name__
                object_id = instance.pk
            except:
                application_name = None
                model_name = None
                object_id = None
            finally:
                related_object_data = {
                    'app_name': application_name,
                    'model_name': model_name,
                    'object_representation': object_representation,
                    'object_id': object_id}
                # Return collected data:
                return related_object_data
    else:
        # Raise type error if instance doesn't inherits from BaseModel class:
        raise TypeError('Provided instance value is not valid object.')
