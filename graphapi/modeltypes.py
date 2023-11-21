from graphene_django import DjangoObjectType

from restapi.models import Me, Project, Pricing, Skill, Contact


class MeType(DjangoObjectType):
    class Meta:
        model = Me


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project


class PricingType(DjangoObjectType):
    class Meta:
        model = Pricing


class SkillType(DjangoObjectType):
    class Meta:
        model = Skill


class ContactType(DjangoObjectType):
    class Meta:
        model = Contact