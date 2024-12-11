#include "lists.h"

/**
 * check_cycle : Function to check if a ;inked list has a cycle
 * @lists: the linked list
 * Return: 1 if cycle is present and 0 if no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	fast = list;
	slow = list;
	

	while (fast != NULL && fast->next !=NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
		return 1; 
		}

	}
	return 0;
}
