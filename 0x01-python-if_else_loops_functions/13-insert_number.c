#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "lists.h"

/**
 * insert_node - adds a new node to a sorted listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *newNode = malloc(sizeof(listint_t));
	int idx = 0, flag = 0;

	if (!newNode)
		return (NULL);
	newNode->n = number;
	newNode->next = NULL;
	if (*head == NULL)
	{
		*head = newNode;
		return (*head);
	}
	for (; newNode->n > temp->n; temp = temp->next)
	{
		if (temp->next == NULL)
		{
			flag = 1;
			break;
		}
		idx++;
	}
	if (!temp->next && flag == 1)
	{
		temp->next = newNode;
		return (temp);
	}
	temp = *head;
	if (idx == 0)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}
	for (; idx != 1; idx--)
		temp = temp->next;
	newNode->next = temp->next;
	temp->next = newNode;
	return (newNode);
}
