from django.shortcuts import render
from api.models import CustomUser, Game , SquadRequest
from api.serializers import UserSerializer, GameSerializer, SquadSerializer
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

def index(request):
    return render(request, "dashboard.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def crear_squad(request):
    return render(request, "crear_squad.html")

def games(request):
    return render(request, "games.html")

class RegisterView(generics.CreateAPIView):
    queryset= CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes= [AllowAny]

class GameList(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes= [AllowAny]

class SquadList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = SquadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = SquadRequest.objects.all()
        game_slug = self.request.query_params.get("game_slug")
        if game_slug:
            queryset = queryset.filter(game__slug=game_slug)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class SquadDetail(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = SquadRequest.objects.all()
    serializer_class = SquadSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):

        instance = self.get_object()
        if instance.creator != request.user:
            return Response(
                {"detail":"No tienes permiso para borrar este anuncio"},
                status=status.HTTP_403_FORBIDDEN
            )
        return self.destroy(request, *args, **kwargs)

def stats(request):
    return render(request, "stats.html")

class SquadStatsApiView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request):
        squads = SquadRequest.objects.all()
        total_squads = squads.count()

        conteo_diario = {}
        for s in squads:
            fecha = str(s.created_at.date())
        if fecha in conteo_diario:
            conteo_diario[fecha] += 1
        else:
            conteo_diario[fecha] = 1

        daily_data = []
        for fecha, cuenta in conteo_diario.items():
            daily_data.append({"date":fecha, "count": cuenta})

        return Response({
            "total_squads": total_squads,
            "daily_stats": daily_data
        })


