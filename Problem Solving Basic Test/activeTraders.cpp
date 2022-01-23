#include <bits/stdc++.h>

using namespace std;

vector<string> mostActive(vector<string> customers)
{
    map<string, int> Map;
    for (int i = 0; i < customers.size(); i++)
    {
        if (Map.find(customers[i]) != Map.end())
            Map[customers[i]]++;
        else
            Map.insert(pair<string, int>(customers[i], 1));
    }
    int n = customers.size();
    vector<string> res;
    for (auto i = Map.begin(); i != Map.end(); i++)
    {
        if (i->second * 20 >= n)
            res.push_back(i->first);
    }
    sort(res.begin(), res.end());
    return res;
}