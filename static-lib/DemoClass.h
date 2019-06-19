#pragma once

#include <string>


#if defined(_MSC_VER)
	#define SO_IMPORT __declspec(dllimport)
	#define SO_EXPORT __declspec(dllexport)
#else
	#define SO_IMPORT
	#define SO_EXPORT
#endif

class SO_EXPORT DemoClass
{
public:
	DemoClass();
	~DemoClass();
	void PrintMessage(const std::string& message);
};

