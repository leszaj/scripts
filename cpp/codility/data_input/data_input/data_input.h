#include <iostream>
#include <string>
#include <vector>

using namespace std;

static vector<vector<int>> data_int;
static vector<vector<string>> data_str;

static vector<string> data_tags_all;
static vector<string> data_tags_control;
static vector<vector<string>> data_str_all;
static vector<vector<string>> data_str_control;


struct data_strct
{
};

/*
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

string check_data()
{
    string ret = "";
    std::vector<string>::iterator it;
    int x = 0;

    for (const vector<int>& set_of_nums : data_all) {
        for (const int& num : set_of_nums) {
            //itr_in_tags_all = data_tags_all.find(tg);
            //it = find(data_tags_all.begin(), data_tags_all.end(), tg);

            //if (data_str_all[itr_in_tags_all][itr_dt] != data_str_control[itr_tg][itr_dt])

            //itr_dt++;

            ret += std::to_string(x);
        }
    }

    return ret;
}

*/

/*********************************************/
/****************** GETTERS ******************/
/*********************************************/
vector<int> get_data_int(string line)
{
    vector<int> data_v;
    string data_str;
    int itr = 0;

    while (itr < line.size())
    {
        data_str = "";
        while ((line[itr] != ',') && (line[itr] != ';') && (line[itr] != ' ') && (line[itr] != '\0')) {
            data_str += line[itr];
            itr++;
        }

        data_v.push_back(atoi(data_str.c_str()));
        itr++;
    }
    return data_v;
}

vector<string> get_data_str(string line)
{
    vector<string> data_v;
    string data;
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

/**********************************************/
/****************** DECODERS ******************/
/**********************************************/

void decode_data_with_tags() {
    string line;
    static bool is_data_collected = false;

    while (getline(cin, line)) {
        if(!is_data_collected ){
            if (data_tags_all.empty()) { data_tags_all = get_data_str(line); }
            data_str_all.push_back(get_data_str(line));

            if (line[0] == '\0'){
                is_data_collected = true;
                continue;
            }
        }
        else {
            if (data_tags_control.empty()) { data_tags_control = get_data_str(line); }
            data_str_control.push_back(get_data_str(line));
        }
    }
}

void decode_data_str(string line)
{
    data_str.push_back(get_data_str(line));
}

void decode_data_int(string line)
{
    data_int.push_back(get_data_int(line));
}

