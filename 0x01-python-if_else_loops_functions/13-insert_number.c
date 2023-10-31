#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	if (!head || !*head)
		return (add_nodeint_end(head, number));
	if ((*head)->n < number)
		if ((*head)->next->n >= number)
		{
			listint_t *new;

			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);

			new->n = number;
			new->next = (*head)->next;
			(*head)->next = new;

			return (new);
		}
		else
			return (insert_node(&(*head)->next, number));
	else
		return (NULL);
}
