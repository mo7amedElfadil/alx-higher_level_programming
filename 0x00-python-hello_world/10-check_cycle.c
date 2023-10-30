#include "lists.h"
/**
 * check_cycle -  finds the loop in a linked list.
 * @list: head of the linked list to be printed
 * Return: 1 if found and zero if not
 */
int check_cycle(listint_t *list)
{
	listint_t *rab = list, *tur = list;

	if (!(list))
		return (0);
	while (rab && tur && rab->next)
	{
		rab = rab->next->next;
		tur = tur->next;
		if (rab == tur)
		{
			tur = list;
			while (rab != tur)
			{
				tur = tur->next;
				rab = rab->next;
			}
			return (1);
		}
	}
	return (0);
}
