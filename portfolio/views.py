from django.shortcuts import render, HttpResponse
from .models import MeContrate
from django.http import JsonResponse
import json

def home(request):
    return render(request, 'home.html')


def contrato(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        servico = body.get('options')
        print(servico)
        nome = body.get('nome')
        email = body.get("email")
        mensagem = body.get('mensagem')
        
        servico_formatado = ', '.join(servico)

        # print(servico, nome, email,mensagem)
        new_mecontrate = MeContrate.objects.create(
            servico = servico_formatado,
            nome = nome,
            email = email,
            mensagem = mensagem
        )
        new_mecontrate.save()
        
        response_data = {'message': 'Formulário enviado com sucesso!'}
        return JsonResponse(response_data)
    

def dashboard(request):
    contratos = MeContrate.objects.exclude(lido=True)

    lidos = MeContrate.objects.exclude(lido=False)
    
    context={
        'contratos':contratos,
        'lidos':lidos,
        }
    return render(request, 'admin.html', context)


def excluir_mensagem(request, contato_id):
    try:
        contato = MeContrate.objects.get(pk=contato_id)
        contato.delete()
        return JsonResponse({"success": True})
    except MeContrate.DoesNotExist:
        return JsonResponse({"success": False, "error": "Contato não encontrado"})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})

def marcar_como_lido(request, contato_id):
    try:
        contato = MeContrate.objects.get(id=contato_id)
        contato.lido = True
        contato.save()
        return JsonResponse({"success": True})
    
    except MeContrate.DoesNotExist:
        return JsonResponse({"success": False, "error": "Contato não encontrado"})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})

def marcar_como_nao_lido(request, contato_id):
    try:
        contato = MeContrate.objects.get(id=contato_id)
        contato.lido = False
        contato.save()
        return JsonResponse({"success": True})
    
    except MeContrate.DoesNotExist:
        return JsonResponse({"success": False, "error": "Contato não encontrado"})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})