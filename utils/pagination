from rest_framework import pagination, response, status
from rest_framework.exceptions import APIException


class NotFound(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = ('bad_request.')
    default_code = 'bad_request'


class CustomPagination(pagination.PageNumberPagination):

    def paginate_queryset(self, queryset, request, view=None):
        """
        Paginate a queryset if required, either returning a
        page object, or `None` if pagination is not configured for this view.
        """
        page_size = self.get_page_size(request)
        if not page_size:
            return None

        paginator = self.django_paginator_class(queryset, page_size)
        page_number = request.query_params.get(self.page_query_param, 1)
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages

        try:
            self.page = paginator.page(page_number)
        except Exception as exc:
            # Here it is
            msg = {
                "status": False,
                "message": "Page out of range"
            }
            raise NotFound(msg)

        if paginator.num_pages > 1 and self.template is not None:
            # The browsable API should display pagination controls.
            self.display_page_controls = True

        self.request = request
        return list(self.page)

    # Customization default response
    def get_paginated_response(self, data):
        next_page = self.get_next_link()
        prev_page = self.get_previous_link()
        # print(f"Next page: {next_page}")
        # print(f"Prev page: {prev_page}")
        if next_page is None and prev_page is None:
            return response.Response({
                # 'next': 0,
                # 'previous': 0,
                # 'count': self.page.paginator.count,
                "message": "Data successfully returned",
                'status': True,
                'issue': data,
            })
        else:
            return response.Response({
                # 'next': self.get_next_link(),
                # 'previous': self.get_previous_link(),
                # 'count': self.page.paginator.count,
                "message": "Data successfully returned",
                'status': True,
                'issue': data,
            })


