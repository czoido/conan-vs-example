#pragma once

#include <string>

#if defined(_USRDLL)
	#define DLLEXPORT __declspec(dllexport)
#else
	#if defined(_LIB) || defined(LINK_STATIC_LIB)
		#define DLLEXPORT
	#elif defined(LINK_DYNAMIC_LIB)
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

