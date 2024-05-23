from django.shortcuts import render
from django.http import HttpResponse
import qrcode
import io

def index(request):
    return render(request, 'index.html')

def generate_qr(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(input_text)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')

        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)

        return HttpResponse(buf, content_type='image/png')
    return HttpResponse("Invalid request", status=400)
