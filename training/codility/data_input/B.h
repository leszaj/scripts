#include <iostream>
#include <string>
#include <vector>

using namespace std;

static vector<vector<int>> data_all;


struct data_strct
{
};

string check_data() 
{ 
    string ret = "";
    std::vector<string>::iterator it;
    int x = 0;

    for (const vector<int>& set_of_nums : data_all)    {
        for (const int& num : set_of_nums)        {




            //itr_in_tags_all = data_tags_all.find(tg);
            //it = find(data_tags_all.begin(), data_tags_all.end(), tg);

            //if (data_str_all[itr_in_tags_all][itr_dt] != data_str_control[itr_tg][itr_dt])

            //itr_dt++;

            ret += std::to_string(x);
        }
    }

    return ret;
}

vector<int> get_data(string line)
{
    vector<int> data_v;
    int data = 0;
    string data_str;
    int itr = 0;

    //while (line[itr] != '\0')
    while (itr < line.size())
    {
        data_str = "";
        while ((line[itr] != ' ') && (line[itr] != '\0')) {
            data_str += line[itr];
            itr++;
        }

        data_v.push_back(atoi(data_str.c_str()));
        itr++;
    }
    return data_v;
}

int main()
{
    string line;
    bool is_data_collected = false;

    while (getline(cin, line))
        data_all.push_back(get_data(line));
       // cout << line << endl;

    cout << check_data() << endl;
}

