
#include <map>
#include <limits>
#include <exception>


struct mapa_interwalow
{
    mapa_interwalow() = delete;

    mapa_interwalow(char init) { map_[std::numeric_limits<int>::lowest()] = init; }

    void powiaz_interwal(int begin, char value) 
    {
        auto active_range = std::prev(map_.upper_bound(begin));
        if (active_range == map_.end())                     // jakiœ zakres musi byæ - w przeciwnym wypadku b³¹d
            throw "Fatal error: cannot find begin range for specific index";

        if (active_range->second == value)
            return;

        auto prev_value_range = std::prev(active_range);
        if (active_range->first == begin && prev_value_range != map_.end() && prev_value_range->second == value)
            map_.erase(active_range);
        else
            map_[begin] = value;
    }

    void powiaz_interwal(int begin, int end, char value) 
    {
        if (begin == end)
            return;

        auto active_range_begin = std::prev(map_.upper_bound(begin));
        if (active_range_begin == map_.end())               // jakiœ zakres musi byæ - w przeciwnym wypadku b³¹d
            throw "Fatal error: cannot find begin range for specific index";

        auto active_range_end = std::prev(map_.upper_bound(end));
        if (active_range_end == map_.end())                 // jakiœ zakres musi byæ - w przeciwnym wypadku b³¹d
            throw "Fatal error: cannot find begin range for specific index";

        char backup = active_range_end->second;
        if (active_range_end == active_range_begin) {
            if (active_range_end->second == value)
                return;

            auto prev_value_range = std::prev(active_range_begin);
            if (prev_value_range != map_.end() && prev_value_range->second == value)
                map_.erase(active_range_begin);
            else
                map_[begin] = value;
            map_[end] = backup;
        }
        else {
            auto beginIt = active_range_begin;
            auto endIt = active_range_end;
            bool setNewBegin = false;
            bool setNewEnd = false;
            if (active_range_begin->first == begin) {
                auto prev_begin_range = std::prev(active_range_begin);
                if (prev_begin_range != map_.end() && prev_begin_range->second != value) {
                    active_range_begin->second = value;
                    ++beginIt;
                }
            }
            else {
                ++beginIt;
                setNewBegin = active_range_begin->second != value;
            }

            if (active_range_end->first == end) {
                if (active_range_end->second == value)
                    ++endIt;
            }
            else {
                ++endIt;
                setNewEnd = active_range_begin->second != value;
            }

            map_.erase(beginIt, endIt);

            if (setNewBegin)
                map_[begin] = value;
            if (setNewEnd)
                map_[end] = backup;
        }
    }

    char sprawdz_wartosc(int idx) const {
        auto find_range = std::prev(map_.upper_bound(idx));
        if (find_range == map_.end())                   // jakiœ zakres musi byæ - w przeciwnym wypadku b³¹d
            throw "Fatal error: cannot find begin range for specific index";
        return find_range->second;
    }

    void print(int begin, int end) const {
        if (end >= begin) {
            for (int i = begin; i <= end; ++i)
                std::cout << i << " " << sprawdz_wartosc(i) << " size: " << map_.size() << std::endl;
            std::cout << std::endl;
        }
    }

private:
    std::map<int, char> map_;
};

