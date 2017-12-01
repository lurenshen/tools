// WriteMessage.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include "addressbook.pb.h"
using namespace std;

int main(int argc, char* argv[]) {
	string addrStr("");
	address_book::AddressBook addBook;
	char iStr[10] = {'\0'};

	// 10个人的信息
	for (int i = 0; i < 10; i++)
	{
		address_book::Person* person = addBook.add_people();
		person->set_name(string("xiaoming"));
		person->set_id(i);
		person->set_email(string("xiaoming@qq.com"));
		//每个人设置三个电话号码
		for (int j = 0; j < 3; j++)
		{
			address_book::Person_PhoneNumber* phoneNum = person->add_phones();
			_itoa_s(j, iStr, 10);
			phoneNum->set_number(string("10000") + string(iStr));
			phoneNum->set_type(address_book::Person_PhoneType(j));
		}
	}

	addBook.SerializeToString(&addrStr);

	cout << "------------------addBook content begin--------------\n" << addrStr << "\n------------------addBook content end--------------\n";

	return 0;
}

