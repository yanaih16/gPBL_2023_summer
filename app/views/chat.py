from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from ..models import Chat, User
def chat(request,id):
    user=request.user
    receiver=User.objects.get(id=id)
    chat_sender=Chat.objects.filter(sender=user,receiver=receiver)
    chat_receive=Chat.objects.filter(sender=receiver,receiver=user)
    user2 = User.objects.all()
    data={
        'receiver':User.objects.get(id=id),
        'sender':request.user
    }
    return render(request,'chat/chat.html',{'data':data,'chat_sender':chat_sender,'chat_receive':chat_receive, 'user_list':user2})
def com(request):
    sender = request.user
    receiver=User.objects.get(username=request.POST.get('receiver'))
    chat=request.POST.get('msg')
    Chat.objects.create(receiver=receiver,sender=sender,text=chat)

    return JsonResponse('hit',safe=False)
def receive_data(request):
    user=request.user
    receiver = User.objects.get(username=request.POST.get('receiver'))
    a= Chat.objects.filter(receiver=user, sender=receiver).last()
    data={'id':a.id,'chat':a.text}
    return JsonResponse(data)
def all_user(request):
    user=User.objects.all()
    return render(request,'chat/user.html',{'user_list':user})