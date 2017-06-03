from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Templates
    url(r'^tictactoe', 'controllers.views.tictactoe', name='tictactoe'),
    url(r'^sendPlay/(?P<index>\d+)/(?P<player>\w+)/(?P<shoot>\d+)/(?P<board>\w+)', 'controllers.views.sendPlay', name='sendPlay'),
    
    
)