#pragma once

#include <string>

#ifdef _USRDLL
	#define DLLEXPORT __declspec(dllexport)
#else
	#ifdef _LIB
		#define DLLEXPORT
	#else
		#define DLLEXPORT __declspec(dllimport)
	#endif
#endif

class DLLEXPORT DemoClass
{
public:
	DemoClass();
	~DemoClass();
	void PrintMessage(const std::string& message);
};

