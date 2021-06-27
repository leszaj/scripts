#include <iostream>
#include <string>
#include <vector>

using namespace std;


static vector<string> data_tags_all;
static vector<string> data_tags_control;

static vector<vector<string>> data_str_all;
static vector<vector<string>> data_str_control;


struct data_strct
{
};

bool check_data() 
{ 
    bool ret = true;
    int itr_tg = 0, itr_dt = 0, itr_in_tags_all = 0;
    std::vector<string>::iterator it;
    

    string data_to_be_compared;

    for (const string& tg : data_tags_control)  // wszystkie tagi kontrolne
    {
        for (const vector<string>& dt : data_str_control)   // wszystkie zestawy danych
        {
            //itr_in_tags_all = data_tags_all.find(tg);
            //it = find(data_tags_all.begin(), data_tags_all.end(), tg);

            if (data_str_all[itr_in_tags_all][itr_dt] != data_str_control[itr_tg][itr_dt])
                ret = false;

            itr_dt++;
        }

        itr_tg++;
    }

    return ret;
}

vector<string> get_data(string line)
{
    vector<string> data_v;
    string data;
    bool is_ok = false;
    int itr = 0;

    while (line[itr] != '\0')
    {
        data = "";

        while ((line[itr] != ',') && (line[itr] != '\0')) {
            data += line[itr];
            itr++;
        }

        data_v.push_back(data);
        itr++;
    }
    return data_v;
}

int main() {
    string line;
    bool is_data_collected = false;

    while (getline(cin, line)) {

        if(!is_data_collected ){
            if (data_tags_all.empty())
                data_tags_all = get_data(line);

            // collect the data here
            data_str_all.push_back(get_data(line));

            if (line[0] == '\0'){
                is_data_collected = true;
                continue;
            }
        }
        else // control_data
        {
            if (data_tags_control.empty())
                data_tags_control = get_data(line);

            // collect the data here
            data_str_control.push_back(get_data(line));
        }
       // cout << line << endl;
    }

    cout << check_data() << endl;
}

