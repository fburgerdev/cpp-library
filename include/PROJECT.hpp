#pragma once
// common.hpp (BEGIN)
#include <memory> // address, int, uint
#include <string> // string
#include <string_view> // string_view
#include <array> // Array
#include <vector> // List
#include <stack> // Stack
#include <queue> // Queue
#include <deque> // Deque
#include <unordered_set> // Set 
#include <map> // Map
#include <set> // HashSet
#include <unordered_map> // HashMap

namespace PROJECT {
    // Types
    // Types :: address
    using address = std::size_t;
    // Types :: int
    using int8 = std::int8_t;
    using int16 = std::int16_t;
    using int32 = std::int32_t;
    using int64 = std::int64_t;
    // Types :: uint
    using uint8 = std::uint8_t;
    using uint16 = std::uint16_t;
    using uint32 = std::uint32_t;
    using uint64 = std::uint64_t;
    // Types :: string
    using string = std::string;
    // Types :: string_view
    using string_view = std::string_view;
    // Container
    // Container :: Sequence
    template<typename T, address N>
    using Array = std::array<T, N>;
    template<typename T>
    using List = std::vector<T>;
    template<typename T>
    using Stack = std::stack<T>;
    template<typename T>
    using Queue = std::queue<T>;
    template<typename T>
    using Deque = std::deque<T>;
    // Container :: Tree
    template<typename T>
    using Set = std::set<T>;
    template<typename Key, typename Value>
    using Map = std::map<Key, Value>;
    // Container :: Hash
    template<typename T>
    using HashSet = std::unordered_set<T>;
    template<typename Key, typename Value>
    using HashMap = std::unordered_map<Key, Value>;
}
// common.hpp (END)