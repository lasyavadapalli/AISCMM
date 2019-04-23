using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Globalization;
using System.Linq;
using System.Reflection;
using System.Resources;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace AISCM
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class MasterDetailPage1Master : ContentPage
    {
        public ListView ListView;

        public MasterDetailPage1Master()
        {
            InitializeComponent();

            BindingContext = new MasterDetailPage1MasterViewModel();
            ListView = MenuItemsListView;
        }

        class MasterDetailPage1MasterViewModel : INotifyPropertyChanged
        {
            public ObservableCollection<MasterDetailPage1MenuItem> MenuItems { get; set; }

            public MasterDetailPage1MasterViewModel()
            {
                string ResourceId = "AISCM.Resources.AppResource";
                if (Global_portable.default_language != null)
                {
                    CultureInfo.DefaultThreadCurrentCulture = new CultureInfo(Global_portable.default_language);
                    ResourceManager resourceManager = new ResourceManager(ResourceId, typeof(TranslateExtension).GetTypeInfo().Assembly);
                    //System.Diagnostics.Debug.WriteLine(" " + Title + " " + resourceManager.GetString("Home", CultureInfo.DefaultThreadCurrentCulture));
                    MenuItems = new ObservableCollection<MasterDetailPage1MenuItem>(new[]
                {
                    new MasterDetailPage1MenuItem { Id = 0, Title =  resourceManager.GetString("Home", CultureInfo.DefaultThreadCurrentCulture)},
                    new MasterDetailPage1MenuItem { Id = 1, Title =  resourceManager.GetString("Your Farm", CultureInfo.DefaultThreadCurrentCulture)},
                    new MasterDetailPage1MenuItem { Id = 2, Title = resourceManager.GetString("Water Tank Status", CultureInfo.DefaultThreadCurrentCulture) },
                    new MasterDetailPage1MenuItem { Id = 3, Title = resourceManager.GetString("Change Language", CultureInfo.DefaultThreadCurrentCulture) },
                    new MasterDetailPage1MenuItem { Id = 4, Title = resourceManager.GetString("Update PH", CultureInfo.DefaultThreadCurrentCulture) },
                    new MasterDetailPage1MenuItem { Id = 5, Title = resourceManager.GetString("Schemes", CultureInfo.DefaultThreadCurrentCulture) },
                    new MasterDetailPage1MenuItem { Id = 6, Title = resourceManager.GetString("Farm Data", CultureInfo.DefaultThreadCurrentCulture)},
                    new MasterDetailPage1MenuItem { Id = 7, Title = resourceManager.GetString("Logout", CultureInfo.DefaultThreadCurrentCulture) },
                });
                }
                else
                {
                    MenuItems = new ObservableCollection<MasterDetailPage1MenuItem>(new[]
                {
                    new MasterDetailPage1MenuItem { Id = 0, Title =  "Home" },
                    new MasterDetailPage1MenuItem { Id = 1, Title =  "Your Farm"},
                    new MasterDetailPage1MenuItem { Id = 2, Title = "Water Tank Status"},
                    new MasterDetailPage1MenuItem { Id = 3, Title = "Change Language" },
                    new MasterDetailPage1MenuItem { Id = 4, Title = "Update PH"},
                    new MasterDetailPage1MenuItem { Id = 5, Title = "Schemes"},
                    new MasterDetailPage1MenuItem { Id = 6, Title = "Farm Data"},
                    new MasterDetailPage1MenuItem { Id = 7, Title = "Logout"},
                });
                }
            }

            #region INotifyPropertyChanged Implementation
            public event PropertyChangedEventHandler PropertyChanged;
            void OnPropertyChanged([CallerMemberName] string propertyName = "")
            {
                if (PropertyChanged == null)
                    return;

                PropertyChanged.Invoke(this, new PropertyChangedEventArgs(propertyName));
            }
            #endregion
        }
    }
}