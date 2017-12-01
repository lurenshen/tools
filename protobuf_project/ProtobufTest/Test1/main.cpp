//#include "proto/addressbook.pb.h"
#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

#ifndef _SECURE_SCL
#define _SECURE_SCL 0
#else
#undef _SECURE_SCL
#define _SECURE_SCL 0
#endif

int main()
{
	//string addrStr("");
	//address_book::AddressBook addBook;
	//char iStr[10] = { '\0' };

	//// 10个人的信息
	//for (int i = 0; i < 10; i++)
	//{
	//	address_book::Person* person = addBook.add_people();
	//	person->set_name(string("xiaoming"));
	//	person->set_id(i);
	//	person->set_email(string("xiaoming@qq.com"));
	//	//每个人设置三个电话号码
	//	for (int j = 0; j < 3; j++)
	//	{
	//		address_book::Person_PhoneNumber* phoneNum = person->add_phones();
	//		_itoa_s(j, iStr, 10);
	//		phoneNum->set_number(string("10000") + string(iStr));
	//		phoneNum->set_type(address_book::Person_PhoneType(j));
	//	}
	//}

	//addBook.SerializeToString(&addrStr);

	//cout << "------------------addBook content begin--------------\n" << addrStr << "\n------------------addBook content end--------------\n";


	getchar();
	return 0;
}