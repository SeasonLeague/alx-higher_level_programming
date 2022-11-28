#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: lsit parameter
 *
 * Return: 1 if the list has cycle, 0 if it doesnt
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;


	if (!list)
	{
		return (0);
	}
	while (fast && slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
