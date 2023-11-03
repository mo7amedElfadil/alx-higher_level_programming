#include "lists.h"


/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the linked list to be printed
 * Return: 1 if palindrome and zero if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *rev = NULL;

	if (!head || !(*head) || !(*head)->next)
		return (1);
	rev = reverse_listint(head);
	while (*head && rev)
	{
		if ((*head)->n != rev->n)
			return (0);
		(*head) = (*head)->next;
		rev = rev->next;
	}

	return (1);
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
