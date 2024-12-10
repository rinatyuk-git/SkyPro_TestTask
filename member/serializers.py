from rest_framework import serializers

from member.models import Product, Member


class ProductSerializer(serializers.ModelSerializer):
    """ Creation of Product's serializer """

    class Meta:
        model = Product
        fields = "__all__"


class MemberSerializer(serializers.ModelSerializer):
    """ Creation of Member's serializer """

    def validate(self, data):  # Comparison of member_type for new Member vs Supplier member_type
        supplier_for_member = data.get('supplier_for_member')
        member_type = data.get('member_type')
        if member_type == supplier_for_member.member_type:
            raise serializers.ValidationError(
                f"Member's type of the supplier cannot match with the member's type of the new member."
                f"Type of the supplier: {supplier_for_member.member_type}, type of actual Member: {member_type}"
            )
        return data

    class Meta:
        model = Member
        fields = "__all__"


class MemberUpdateSerializer(serializers.ModelSerializer):
    """ Creation serializer for updates of Member """

    class Meta:
        model = Member
        fields = "__all__"

    def validate(self, data):  # checking for update of debt_to_supplier
        if 'member_debt_to_supplier' in data:
            raise serializers.ValidationError({"member_debt_to_supplier": "This field cannot be changed."})

        instance = self.instance  # Comparison of member_type for new Member vs Supplier member_type
        supplier_for_member = data.get('supplier_for_member', instance.supplier_for_member)
        member_type = data.get('member_type', instance.member_type)
        if supplier_for_member.member_type == member_type:
            raise serializers.ValidationError(
                f"Member's type of the supplier cannot match with the member's type of the new member."
                f"Type of the supplier: {supplier_for_member.member_type}, type of actual Member: {member_type}"
            )

        return data

# class MemberUpdateSerializer(serializers.ModelSerializer):
#     """ Checking for update of debt_to_supplier """
#
#     def validate(self, data):  # checking for update of debt_to_supplier
#         if 'member_debt_to_supplier' in data:
#             raise serializers.ValidationError({"member_debt_to_supplier": "This field cannot be changed."})
#
#     class Meta:
#         model = Member
#         fields = "__all__"
