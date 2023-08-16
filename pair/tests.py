from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Pair


class PairTests(APITestCase):
    def test_create_pair(self):
        url = reverse('pair:make_pair-list')
        data = {
            'pair_request':"this is my report",
            'date':'2000-10-10',
            # 'assistant_confirm' : True,
        }
        response = self.client.post(url,data,format='json')
        self.assertEqual(Pair.objects.count(),1)
        self.assertEqual(response.status_code,200)
        # self.assertEqual(Pair.objects.get(cost=2000).pair_request,'my truck have trouble')
        

    # pair_request = models.OneToOneField(Driver,on_delete=models.CASCADE)
    # date = models.DateField(auto_now_add=True)
    # cost = models.BigIntegerField(null=True, blank=True)
    # assistant_confirm = models.BooleanField(default=False,blank=True)   
    # payed = models.BooleanField (default=False)   