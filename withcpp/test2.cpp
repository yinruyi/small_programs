#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
using namespace boost::python;

int main(const int x, const int y)
{
    return x + y;
}

int Del(const int x, const int y)
{
    return x - y;
}

BOOST_PYTHON_MODULE(test2)
{
    def("main", main);
    def("Del", Del);
}