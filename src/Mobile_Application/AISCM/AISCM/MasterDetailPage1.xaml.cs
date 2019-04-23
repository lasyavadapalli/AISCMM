using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Reflection;
using System.Resources;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace AISCM
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class MasterDetailPage1 : MasterDetailPage
    {
        public MasterDetailPage1()
        {
            InitializeComponent();
            MasterPage.ListView.ItemSelected += ListView_ItemSelected;
        }

        private void ListView_ItemSelected(object sender, SelectedItemChangedEventArgs e)
        {
            var item = e.SelectedItem as MasterDetailPage1MenuItem;
            if (item == null)
                return;

             var page = (Page)Activator.CreateInstance(item.TargetType);
            page.Title = item.Title;
            if(item.Title == "Home" || item.Title== "घर")
            {
                Detail = new NavigationPage(new index());
                IsPresented = false;
            }
            else if (item.Title == "Water Tank Status" || item.Title == "पानी की टंकी की स्थिति")
            {
                Detail = new NavigationPage(new display_water_related_data());
                IsPresented = false;
            }
            else if (item.Title == "Update PH" || item.Title == "PH को अपडेट करें")
            {
                Detail = new NavigationPage(new FarmDetails());
                IsPresented = false;
            }
            else if (item.Title == "Change Language" || item.Title == "भाषा बदलो")
            {
                Detail = new NavigationPage(new set_language());
                IsPresented = false;
            }
            else if (item.Title == "Schemes" || item.Title == "योजनाएं")
            {
                Detail = new NavigationPage(new Demo());
                IsPresented = false;
            }
            else if(item.Title == "Farm Data" || item.Title == "फार्म डेटा")
            {
                Detail = new NavigationPage(new FarmData());
                IsPresented = false;
            }
            else if(item.Title == "Your Farm" || item.Title == "आपका खेत")
            {
                Detail = new NavigationPage(new FarmLayout());
                IsPresented = false;
            }
            else if(item.Title == "Logout" || item.Title == "ऐप से लॉगआउट करें")
            {
                Global_portable.email = "";
                Global_portable.user_id = 0;
                DependencyService.Get<call_web_service>().startLoginActivity();
                IsPresented = false;
            }
            else
            {
                DependencyService.Get<call_web_service>().startLoginActivity();
                System.Diagnostics.Debug.WriteLine("page not found....");
            }

            MasterPage.ListView.SelectedItem = null;
        }
    }
}