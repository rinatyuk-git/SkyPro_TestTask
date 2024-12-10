from django.contrib import admin

from member.models import Product, Member


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "product_name", "product_model", "product_launched_at",)
    list_filter = ("product_name",)
    search_fields = ("product_name", "product_model",)


@admin.action(description="Clearing of debt to supplier")
def do_clearing(modeladmin, request, queryset):
    """ Do clearing of the debt to supplier """
    queryset.update(member_debt_to_supplier=0)


class MemberAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "member_name",
        "member_debt_to_supplier",
        "supplier_for_member",
        "member_country",
        "member_city",
    ]
    ordering = ["member_name"]
    list_filter = (
        "member_city",
    )
    readonly_fields = ('member_debt_to_supplier', 'member_level',)
    actions = [do_clearing]


admin.site.register(Member, MemberAdmin)
