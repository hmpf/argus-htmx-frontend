from argus.auth.models import SubclassMixin, Preferences, PreferencesManager

from .forms import PreferencesForm


class ArgusHtmxPreferencesManager(PreferencesManager):
    def get_queryset(self):
        return super().get_queryset().filter(namespace=NAMESPACE)

    def create(self, **kwargs):
        kwargs["namespace"] = NAMESPACE
        return super().create(**kwargs)


class ArgusHtmxPreferences(SubclassMixin, Preferences):
    class Meta:
        proxy = True

    app_label = "argus_htmx"
    class_name = "ArgusHtmxPreferences"
    FORM = PreferencesForm

    objects = ArgusHtmxPreferencesManager()


NAMESPACE = ArgusHtmxPreferences.generate_namespace()


# def preference_subclass_factory(app_label, class_name, form):
#     class _tmp(SubclassMixin):
#         pass
#     _tmp.app_label = app_label
#     _tmp.class_name = class_name
#
#     NAMESPACE = _tmp.generate_namespace()
#
#     class Manager(PreferencesManager):
#         def get_queryset(self):
#             return super().get_queryset().filter(namespace=NAMESPACE)
#
#         def create(self, **kwargs):
#             kwargs["namespace"] = NAMESPACE
#             return super().create(**kwargs)
#
#     class Proxy(SubclassMixin, Preferences):
#         objects = Manager()
#
#         class Meta:
#             proxy = True
#
#     Proxy.app_label = app_label
#     Proxy.class_name = class_name
#     Proxy.FORM = form
#
#     return Proxy
#
#
# ArgusHtmxPreferences = preference_subclass_factory("argus_htmx", "ArgusHtmxPreferences", PreferencesForm)
