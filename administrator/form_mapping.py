from administrator.forms import GroupForm, GroupFormSuper, CountryForm, InternationalregionForm, SiteSettingsForm, SiteUserForm, SubscriptionPlanForm, UserForm, UserFormSuper
from shohojit.forms import SliderForm

MODEL_FORM_MAPPING = {
    'group': GroupForm,
    'groupsuper': GroupFormSuper,
    'internationalregion': InternationalregionForm,
    'country': CountryForm,
    'usersuper': UserFormSuper,
    'user': UserForm,
    'sitesettings': SiteSettingsForm,
    'siteuser': SiteUserForm,
    'subscriptionplan': SubscriptionPlanForm,
    'slider': SliderForm,
}