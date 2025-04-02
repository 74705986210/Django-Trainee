from django.dispatch import Signal
from django.db import models

my_signal = Signal()

class MyModel(models.Model):
    name = models.CharField(max_length=100)

def signal_receiver(sender, **kwargs):
    print("Signal received!")
    import time
    time.sleep(2)  
    print("Signal processing complete.")

my_signal.connect(signal_receiver)

print("Before sending signal.")
my_signal.send(sender=MyModel)
print("After sending signal.")