#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the linked list to be printed
 * Return: 1 if palindrome and zero if not
 */
int is_palindrome(listint_t **head)
{
	size_t i = 0, mid_len = listint_len(*head) / 2;
	listint_t *mid = *head;

	if (!head || !(*head) || !(*head)->next)
		return (1);
	for (; i < mid_len; i++)
		mid = mid->next;
	mid = reverse_listint(&mid);
	for (; mid && *head; mid = mid->next, (*head) = (*head)->next)
		if (mid->n != (*head)->n)
			return (0);
	return (1);

}
/**
 * listint_len - return number of elements in a listint_t list
 * @h: head of the linked list to be printed
 * Return: number of elements
 */

size_t listint_len(const listint_t *h)
{
	if (!(h))
		return (0);
	return (1 + listint_len(h->next));
}


/**
 * reverse_listint - reverse a listint_t
 * @head: head of the linked list to be printed
 * Return: pointer to first node
 */

listint_t *reverse_listint(listint_t **head)
{
	*head = reverse(head);
	return (*head);
}
/**
 * reverse - reverse a listint_t helper function
 * @head: head of the linked list to be printed
 * Return: pointer to first node
 */
listint_t *reverse(listint_t **head)
{
	listint_t *next = NULL;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (*head);
	}
	next = reverse(&(*head)->next);
	(*head)->next->next = (*head);
	(*head)->next = NULL;
	return (next);
}

