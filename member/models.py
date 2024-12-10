from django.db import models

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):
    product_name = models.CharField(
        max_length=150,
        verbose_name="Product name",
        help_text="Put product name",
    )  # Product name
    product_model = models.CharField(
        max_length=150,
        verbose_name="Product model",
        help_text="Put product model",
    )  # Product model
    product_launched_at = models.DateField(
        verbose_name="Product's launch date",
        help_text="In format 2024-08-04",
    )  # Product's launch date

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['product_name']

    def __str__(self):
        return f'{self.product_name}'


class Member(models.Model):  # member of the sales network

    TYPE_CHOICES = {
        "pl": "plant",
        "rn": "retail_net",
        "rp": "retail_private",
    }

    member_name = models.CharField(
        max_length=150,
        verbose_name="Member's name",
        help_text="Put member's name",
    )  # Member's name
    member_email = models.EmailField(
        verbose_name="Member's contact email",
        help_text="Put member's contact email",
        unique=True,
    )  # Member's email
    member_country = models.CharField(
        max_length=150,
        verbose_name="Member's country",
        help_text="Put member's country",
    )  # Member's country
    member_city = models.CharField(
        max_length=150,
        verbose_name="Member's city",
        help_text="Put member's city",
        **NULLABLE,
    )  # Member's city
    member_street = models.CharField(
        max_length=150,
        verbose_name="Member's street",
        help_text="Put member's street",
        **NULLABLE,
    )  # Member's street
    member_building_no = models.SmallIntegerField(
        verbose_name="Member's building_no",
        help_text="Put member's building_no",
        **NULLABLE,
    )  # Member's building_no
    member_debt_to_supplier = models.DecimalField(
        verbose_name="Member's debt to supplier",
        max_digits=8,
        decimal_places=2,
        **NULLABLE,
    )  # Member's debt to supplier
    member_created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date&Time of Member's creation",
    )  # Date&Time of Member's creation(automatically record at creation)
    member_type = models.CharField(
        max_length=2,
        verbose_name="Member's' type",
        help_text="Put member's type",
        choices=TYPE_CHOICES,
        default="pl",
    )  # Member's' type: plant, retail_net, retail_private
    supplier_for_member = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        **NULLABLE,
    )  # Supplier for the Member: previous network object in the hierarchy
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Product',
        help_text='Choose Product',
        related_name="products",
    )  # Product choosing ManyToManyField
    member_level = models.SmallIntegerField(
        verbose_name="Hierarchy level",
        # help_text="Choose hierarchy level in the trade net",
        **NULLABLE,
    )  # Member's hierarchy level in the trade net: plant-level 0; retail_net-level 1; retail_private-level 2

    def save(self, *args, **kwargs):
        # Plant must have hierarchy member_level 0
        if self.member_type == 'pl':
            self.member_level = 0
        else:
            self.member_level = self.supplier_for_member.member_level + 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Chain member"
        verbose_name_plural = "Chain members"
        ordering = ['member_name']

    def __str__(self):
        return f'{self.member_name}: {self.product}'
