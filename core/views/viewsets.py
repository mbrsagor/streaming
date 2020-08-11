from rest_framework import mixinsfrom rest_framework import filtersfrom django_filters.rest_framework import DjangoFilterBackendclass BaseModelViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,                       mixins.ListModelMixin, mixins.DestroyModelMixin):    """    A viewset that provide default `create()`, `retrieve()`, `update()`, `partial_update()`    `destroy()` and `list()` actions.    """    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)    ordering_fields = '__all__'    def perform_create(self, serializer):        if hasattr(self.product, 'client'):            serializer.save(product=self.request.product)        else:            serializer.save()    def update(self, request, *args, **kwargs):        kwargs['partial'] = True        return super(BaseModelViewSet, self).update(request, *args, **kwargs)