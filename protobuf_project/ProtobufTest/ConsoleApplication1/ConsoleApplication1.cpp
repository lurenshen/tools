// ConsoleApplication1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include "proto/addressbook.pb.h"
#include <fstream>
using namespace std;

//#pragma comment(lib, "libprotobuf.lib")  
//#pragma comment(lib, "libprotoc.lib") 

void PrintAddrBook(address_book::AddressBook &ab)
{
	int psize = ab.people_size();
	cout << "people_size:" << psize << endl;

	for (int i = 0; i < psize; i++)
	{
		address_book::Person person = ab.people(i);
		cout << "-----------person " << i << " info-------------\n";
		cout << "name:" << person.name() << endl;
		cout << "id:" << person.id() << endl;
		cout << "email:" << person.email() << endl;
		cout << "person phone number:\n";
		int phoneNum = person.phones_size();
		for (int j = 0; j < phoneNum; j++)
		{
			address_book::Person_PhoneNumber pn = person.phones(j);
			cout << "number:" << pn.number() << endl;
			cout << "type:" << pn.type() << endl;
		}
	}
}

bool getAddrBook(const string &fileName, address_book::AddressBook &ab)
{
	cout << fileName << endl;
	fstream input("./data/addressBook.txt"/*fileName.c_str()*/, std::fstream::in/* | std::fstream::binary*/);
	bool openFlag = input.is_open();
	if (openFlag)
	{
		if (ab.ParseFromIstream(&input))
		{
			cout << "parse ok\n";
			input.close();
			return true;
		}
		printf("parse error\n");
		input.close();
		return false;
	}
	printf("file open error\n");
	input.close();
	return false;
}

int _tmain(int argc, _TCHAR* argv[])
{
	string addrStr("");
	address_book::AddressBook addBook;
	char iStr[10] = { '\0' };

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
	cout << "------------------addBook content begin--------------\n" << addBook.DebugString() << "\n------------------addBook content end--------------\n";

	/*address_book::AddressBook addBook1;
	addBook1.ParseFromString(addrStr);
	PrintAddrBook(addBook1);*/

	//fstream output("./data/addressBook.txt", std::fstream::out | std::fstream::trunc /*| std::fstream::binary*/);
	//if (output.is_open())
	//{
	//	cout << "file is open\n";
	//	addBook.SerializeToOstream(&output);
	//	//output << addrStr/*addBook.DebugString()*/;
	//	output.close();
	//}

	address_book::AddressBook ab;
	if (getAddrBook(string("./data/addressBook.txt"), ab))
	{
		PrintAddrBook(ab);
	}


	getchar();
	return 0;
}

