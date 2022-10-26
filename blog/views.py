from django.shortcuts import render

# Create your views here.
def index(request):
    # 필요한 코드 넣기
    data = "블로그데이터"
    # render(request, '템플릿 파일', {'키' : 변수값})의 형태
    # 템플릿에서는 '키'가 변수가 되는 것임
    return render(request, 'blog/index.html', {'datas' : data})
