#pragma once

#include <vector>
#include <algorithm>


struct Punkt
{
	int x;
	int y;
};


inline int calcDistance(const Punkt& l, const Punkt& r) { return (l.x - r.x) * (l.x - r.x) + (l.y - r.y) * (l.y - r.y); }


std::vector<Punkt>::iterator get_closest_point(Punkt& p_ref, std::vector<Punkt>& punkty_left)
{
	std::vector<int> distances;
	auto it_ret = punkty_left.begin();

	for (auto it = punkty_left.begin(); it != punkty_left.end(); it++)
	{
		Punkt p = *it;
		distances.push_back(calcDistance(p, p_ref));
		calcDistance(p_ref, *it_ret) > std::min_element(distances.begin(), distances.end())[0] ? it_ret = it : it_ret;
	}

	return it_ret;
}


std::vector<Punkt> lamana(const std::vector<Punkt>& _punkty)
{
	std::vector<Punkt> lamana_ret, punkty_left = _punkty;
	std::vector<Punkt>::iterator it_closest;

	lamana_ret.reserve(_punkty.size());
	lamana_ret.push_back(punkty_left.front());
	punkty_left.erase(punkty_left.begin());

	it_closest = lamana_ret.end() - 1;

	while (!punkty_left.empty())
	{
		it_closest = get_closest_point(*(lamana_ret.end() - 1), punkty_left);
		lamana_ret.push_back(*it_closest);
		punkty_left.erase(it_closest);
	}

	return lamana_ret;
}