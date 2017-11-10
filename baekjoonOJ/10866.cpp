#include <iostream>
#include <deque>
#include <ext/hash_map>

using namespace std;
using namespace __gnu_cxx;

namespace __gnu_cxx{
	template<>
	struct hash<std::string>
	{
		hash<char *> h;
		size_t operator()(const std::string &s) const
		{
			return h(s.c_str());
		};
	};
}

#define CMD_MAX 	8
#define PUSH_BACK	0
#define PUSH_FRONT	1
#define FRONT		2
#define BACK		3
#define SIZE		4
#define EMPTY		5
#define POP_FRONT	6
#define POP_BACK	7

string cmd[] = {"push_back", "push_front", "front", "back",
				 "size", "empty", "pop_front", "pop_back"};

void makeCmdList(hash_map<string ,int> &cmd_map);

bool callCmdFunc(int funcNum, deque<int> &deq, int operand, int &out);

int main(int argc, char *argv[])
{
	hash_map<string ,int> cmd_list;
	makeCmdList(cmd_list);
	
	// solve
	deque<int> deq;
	
	int cmd_cnt;
	cin >> cmd_cnt;
	
	for(int i = 0; i < cmd_cnt; i++){
		string now_cmd;
		int now_operand = 0;
		int out = 0;
		
		cin >> now_cmd;
		if(cmd_list[now_cmd] == PUSH_BACK || cmd_list[now_cmd] == PUSH_FRONT)
			cin >> now_operand;
		if(callCmdFunc(cmd_list[now_cmd], deq, now_operand, out))
			cout << out << endl;
	}
	
}

void makeCmdList(hash_map<string, int> &cmd_map)
{
	for(int i=0; i<CMD_MAX; i++)
		cmd_map[cmd[i]] = i;
}

bool callCmdFunc(int funcNum, deque<int> &deq, int operand, int &out)
{
	bool res = true;
	if(funcNum == PUSH_BACK){
		res = false;
		deq.push_back(operand);
	}
	else if(funcNum == PUSH_FRONT){
		res = false;
		deq.push_front(operand);
	}
	else if(funcNum == FRONT){
		if(deq.empty())
			out = -1;
		else
			out = deq.front();
	}
	else if(funcNum == BACK){
		if(deq.empty())
			out = -1;
		else
			out = deq.back();
	}
	else if(funcNum == SIZE){
		out = deq.size();
	}
	else if(funcNum == EMPTY){
		res = false;
		if(deq.empty())
			cout << true << endl;
		else
			cout << false << endl;
		
	}
	else if(funcNum == POP_FRONT){
		if(deq.empty())
			out = -1;
		else{
			out = deq.front();
			deq.pop_front();
		}
	}
	else if(funcNum == POP_BACK){
		if(deq.empty())
			out = -1;
		else{
			out = deq.back();
			deq.pop_back();
		}
	}

	return res;
}

