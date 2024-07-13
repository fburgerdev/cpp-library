/*
    This header file was automatically created by 'cpp-library',
    it is not meant to be modified.
    For more infos, see https://github.com/fburgerdev/cpp-library
*/
// ranges
#include <ranges> // stdr
// types
#include <memory> // address, int, uint
#include <string> // string
#include <string_view> // strview
// containers
#include <array> // Array
#include <vector> // List
#include <stack> // Stack
#include <queue> // Queue
#include <deque> // Deque
#include <unordered_set> // Set 
#include <map> // Map
#include <set> // HashSet
#include <unordered_map> // HashMap
// function
#include <functional> // function
// optional
#include <optional> // Opt
// stream
#include <iostream> // cout, cerr, endl
#include <fstream> // fstream, ifstream, ofstream
#include <sstream> // strstream
// thread
#include <mutex> // mutex, recursive_mutex, unique_lock
#include <shared_mutex> // shared_mutex, shared_lock
#include <atomic> // atomic dtypes...

namespace __NAMESPACE__ {
    // ranges
    namespace stdr = std::ranges;

    // types
    // :: address
    using address = std::size_t;
    // :: uchar
    using uchar = unsigned char;
    // :: int
    using int8 = std::int8_t;
    using int16 = std::int16_t;
    using int32 = std::int32_t;
    using int64 = std::int64_t;
    // :: uint
    using uint = unsigned int;
    using uint8 = std::uint8_t;
    using uint16 = std::uint16_t;
    using uint32 = std::uint32_t;
    using uint64 = std::uint64_t;
    // :: string
    using string = std::string;
    using strview = std::string_view;

    // container
    // :: sequential
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
    // :: tree
    template<typename T>
    using Set = std::set<T>;
    template<typename Key, typename Value>
    using Map = std::map<Key, Value>;
    // :: hash
    template<typename T>
    using HashSet = std::unordered_set<T>;
    template<typename Key, typename Value>
    using HashMap = std::unordered_map<Key, Value>;

    // move semantics
    using std::forward;
    using std::move;

    // smart pointers
    template<class T, class... Args>
    auto makeUniquePtr(Args&&... args) {
        return std::make_unique<T>(forward(args)...);
    }
    template<class T, class... Args>
    auto makeSharedPtr(Args&&... args) {
        return std::make_shared<T>(forward(args)...);
    }
    template<typename T>
    using UniquePtr = std::unique_ptr<T>;
    template<typename T>
    using SharedPtr = std::shared_ptr<T>;
    template<typename T>
    using WeakPtr = std::weak_ptr<T>;

    // function
    using std::function;

    // templates
    template<typename T>
    using Opt = std::optional<T>;

    // stream
    // :: iostream
    using std::cout;
    using std::cerr;
    using std::endl;
    // :: fstream
    using std::fstream;
    using std::ifstream;
    using std::ofstream;
    // :: stringstream
    using strstream = std::stringstream;

    // thread
    using std::mutex;
    using std::recursive_mutex;
    using std::shared_mutex;
    template<typename Mutex>
    using UniqueLock = std::unique_lock<Mutex>;
    template<typename Mutex>
    using SharedLock = std::shared_lock<Mutex>;

    // atomic
    // :: address
    using atomic_address = std::atomic_size_t;
    // :: int
    using atomic_int = std::atomic_int;
    using atomic_int8 = std::atomic_int8_t;
    using atomic_int16 = std::atomic_int16_t;
    using atomic_int32 = std::atomic_int32_t;
    using atomic_int64 = std::atomic_int64_t;
    // :: uint
    using atomic_uint = std::atomic_uint;
    using atomic_uint8 = std::atomic_uint8_t;
    using atomic_uint16 = std::atomic_uint16_t;
    using atomic_uint32 = std::atomic_uint32_t;
    using atomic_uint64 = std::atomic_uint64_t;
}