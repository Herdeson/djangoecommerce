from django.db import models

# Create your models here.

class CartItemManager(models.Manager):

    def add_item(self, key, product):
        #cart_item, created = self.get_or_create(cart_key=key , product=product, price= product.price) # cuidado que pode ocorrer que o preço esteja alterado
        if self.filter(cart_key = key, product= product).exists():
            created = False
            cart_item = self.get(cart_key = key, product= product)
            cart_item.quantity = cart_item.quantity + 1
            cart_item.save()
        else:
            created = True
            cart_item = CartItem.objects.create(cart_key=key, product = product, price= product.price)
#        if not created:
#            cart_item.quantity = cart_item.quantity + 1
#            cart_item.save()
        return cart_item, created


class CartItem(models.Model):
    cart_key = models.CharField('Chave do carrinho', max_length=40, db_index=True)
    product = models.ForeignKey('catalog.Product', verbose_name='Produto')
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=10)
    objects = CartItemManager()

    class Meta:
        verbose_name = 'Item do Carrinho'
        verbose_name_plural = 'Itens dos Carrinhos'
        unique_together = (('cart_key','product'),)

    def __str__(self):
        return '{} [{}]'.format(self.product, self.quantity)


def post_save_cart_item(instance, **kwargs):
    if instance.quantity < 1 :
        instance.delete()

# Funcao, sender especifica o modelo
models.signals.post_save.connect(post_save_cart_item, sender=CartItem, dispatch_uid='post_save_cart_item')
