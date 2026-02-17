from administrator.forms import GroupForm, GroupFormSuper, CountryForm, InternationalregionForm, SiteSettingsForm, SiteUserForm, SubscriptionPlanForm, UserForm, UserFormSuper
from shohojit.forms import CourseForm, FaqForm, GalleryCategoryForm, GalleryImagesForm, HomeAboutFeatureForm, ServicesForm, SliderForm, TeamCategoryForm, TeamMembersForm, TestimonialsForm, TestimonialsImagesForm, TestimonialsImagesForm

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
    'homeaboutfeature': HomeAboutFeatureForm,
    'testimonials': TestimonialsForm,
    'testimonialsimages': TestimonialsImagesForm,
    'teamcategory': TeamCategoryForm,
    'teammembers': TeamMembersForm,
    'gallerycategory': GalleryCategoryForm,
    'galleryimages': GalleryImagesForm,
    'service': ServicesForm,
    'course': CourseForm,
    'faq': FaqForm,
}