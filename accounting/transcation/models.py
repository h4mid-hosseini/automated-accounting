from django.db import models




class Types(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'type'
        verbose_name_plural = 'types'




class Transactions(models.Model):
    title = models.CharField(max_length=100)
    extra_data = models.TextField(blank=True, null=True)
    price = models.PositiveBigIntegerField()
    is_cost = models.BooleanField(default=True)
    type_of_transaction = models.ForeignKey(Types, on_delete=models.SET_NULL, related_name='transactions', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'transaction'
        verbose_name_plural = 'transactions'
