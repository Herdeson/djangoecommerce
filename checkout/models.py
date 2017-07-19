from django.db import models
from django.conf import settings

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


class OrderManager(models.Manager):

    def create_order(self, user, cart_items):
        order = self.create(user=user)
        for cart_item in cart_items:
            order_item = OrderItem.objects.create(
                order=order, quantity=cart_item.quantity, product=cart_item.product,
                price=cart_item.price
            )
        return order

class Order(models.Model):
    STATUS_CHOICES =(
        (0, 'Aguardando Pagamento'),
        (1, 'Concluída'),
        (2, 'Cancelada'),
    )
    PAYMENT_OPTION_CHOICES = (
        ('deposit', 'Deposito'),
        ('pagseguro', 'PagSeguro'),
        ('paypal', 'Paypal'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário')
    status = models.IntegerField('Situação', choices= STATUS_CHOICES, default=0 , blank=True)
    payment_option = models.CharField('Opção de Pagamento', choices=PAYMENT_OPTION_CHOICES, max_length=20, default = 'deposit')

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado', auto_now=True)

    objects = OrderManager()

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return 'Pedido #{}'.format(self.pk)

    def products(self):
        products_ids = self.items.values_list('product')
        return Product.objects.filter(pk__in=products_ids)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name='Pedido', related_name='items')
    product = models.ForeignKey('catalog.Product', verbose_name='Produto')
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=10)

    class Meta:
        verbose_name = 'Item do Pedido'
        verbose_name_plural= 'Itens dos Pedidos'

    def __str__(self):
        return 'Pedido #{} Produto {}'.format(self.order, self.product)




def post_save_cart_item(instance, **kwargs):
    if instance.quantity < 1 :
        instance.delete()

# Funcao, sender especifica o modelo
models.signals.post_save.connect(post_save_cart_item, sender=CartItem, dispatch_uid='post_save_cart_item')
