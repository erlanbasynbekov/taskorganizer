from django.test import TestCase
from django.urls import reverse, resolve
from task_group.views import (TaskListView, CatagoriesDetailView, CatagoriesCreateView, TaskCreateView, 
                              CatagoriesDeleteView, TaskDeleteView, TaskUpdateView)

class URLRoutingTests(TestCase):

    def test_task_list_url_resolves(self):
        url = reverse('task_group:tlist')
        self.assertEqual(resolve(url).func.view_class, TaskListView)
    
    def test_catagories_detail_url_resolves(self):
        url = reverse('task_group:cdetail', args=['some-str-pk'])
        self.assertEqual(resolve(url).func.view_class, CatagoriesDetailView)
    
    