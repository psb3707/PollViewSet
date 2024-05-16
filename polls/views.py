from rest_framework import viewsets,status
from .models import Poll
from .serializers import PollSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    @action(detail=True,methods=['POST'])
    def agree(self,request,pk):
        poll = Poll.objects.get(id=pk)
        poll.agree = poll.agree+1
        poll.agreeRate = poll.agree/(poll.agree + poll.disagree)
        poll.disagreeRate = poll.disagree/(poll.agree + poll.disagree)
        serializer = PollSerializer(poll)
        poll.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    @action(detail=True,methods=['POST'])
    def disagree(self,request,pk):
        poll = Poll.objects.get(id=pk)
        poll.disagree = poll.disagree+1
        poll.agreeRate = poll.agree/(poll.agree + poll.disagree)
        poll.disagreeRate = poll.disagree/(poll.agree + poll.disagree)
        serializer = PollSerializer(poll)
        poll.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def list(self,request):
        order = request.GET.get('order')
        queryset = self.queryset
        if order:
            if order == 'latest':
                queryset = queryset.order_by('-createAt')
            elif order == 'oldest':
                queryset = queryset.order_by('createAt')
            elif order == 'agree':
                queryset = queryset.order_by('-agree')
            else:
                queryset = queryset.order_by('-disagree')
        serializer = PollSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
       