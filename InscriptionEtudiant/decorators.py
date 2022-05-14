from django.shortcuts import redirect





def notLoggedUsers(view_func):
    def wrapper_func(request , *args , **kwargs):
        #ya9dr ykon endo id wla argument
         if request.user.is_authenticated:
          return redirect('main')
         else:
             return view_func(request , *args , **kwargs)
    return wrapper_func
  

def allowedUsers(allowedGroups=[]):
    def decorator(view_func):
        def wrapper_func(request , *args , **kwargs):   #hadi yakhod les info dyal user
            group = None 
            if request.user.groups.exists():
                group = request.user.groups.all()[0].nom
            if group in allowedUsers:
                return view_func(request , *args , **kwargs) #yt2kd wach y9dr ychofha wla la 
            else:
                return redirect('main/')

        return wrapper_func
    return decorator


def forAdmins(view_func):
        def wrapper_func(request , *args , **kwargs):   #hadi yakhod les info dyal user
            group = None 
            if request.user.groups.exists():
                group = request.user.groups.all()[0].nom
            if group == 'admino':
                return view_func(request , *args , **kwargs) #yt2kd wach y9dr ychofha wla la 

        return wrapper_func


    
    