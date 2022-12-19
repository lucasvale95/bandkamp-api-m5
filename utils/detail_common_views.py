from rest_framework.views import APIView, status, Response, Request
from django.shortcuts import get_object_or_404

class GetDetailView:
    def retrive(self, request: Request, pk: int) -> Response:
        model_object = get_object_or_404(self.view_queryset, pk=pk)

        serializer = self.view_serializer(model_object)

        return Response(serializer.data, status.HTTP_200_OK)

    
class PatchDetailView:
    def update(self, request: Request, pk: int) -> Response:
        model_object = get_object_or_404(self.view_queryset, pk=pk)

        serializer = self.view_serializer(model_object, request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)


class DeleteDetailView:
    def destroy(self, request: Request, pk: int) -> Response:
        model_object = get_object_or_404(self.view_queryset, pk=pk)

        model_object.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class OnlyGetDetailView(GetDetailView, APIView):
    def get(self, request: Request, pk: int) -> Response:
        return super().retrive(request, pk)


class OnlyPatchDetailView(PatchDetailView, APIView):
    def patch(self, request: Request, pk: int) -> Response:
        return super().update(request, pk)


class OnlyDeleteDetailView(DeleteDetailView, APIView):
    def delete(self, request: Request, pk: int) -> Response:
        return super().destroy(request, pk)


class GetPatchDetailView(GetDetailView, PatchDetailView, APIView):
    def get(self, request: Request, pk: int) -> Response:
        return super().retrive(request, pk)

    def patch(self, request: Request, pk: int) -> Response:
        return super().update(request, pk)


class GetPatchDeleteDetailView(GetDetailView, PatchDetailView, DeleteDetailView, APIView):
    def get(self, request: Request, pk: int) -> Response:
        return super().retrive(request, pk)

    def patch(self, request: Request, pk: int) -> Response:
        return super().update(request, pk)

    def delete(self, request: Request, pk: int) -> Response:
        return super().destroy(request, pk)

    