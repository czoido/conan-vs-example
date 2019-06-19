#include "../stdafx.h"
#include "../include/DemoClass.h"

#include <iostream>

DemoClass::DemoClass()
{
}


DemoClass::~DemoClass()
{
}

void DemoClass::PrintMessage(const std::string & message)
{
	#if!defined NDEBUG
		#if!defined _USRDLL
			std::cout << message << " (Debug Static)" << std::endl;
		#else
			std::cout << message << " (Debug Dynamic)" << std::endl;
		#endif
	#else
		#if!defined _USRDLL
			std::cout << message << " (Release Static)" << std::endl;
		#else
			std::cout << message << " (Release Dynamic)" << std::endl;
		#endif
	#endif
}

