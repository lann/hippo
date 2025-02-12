namespace Hippo.Core.Events;

public class CreatedEvent<T> : DomainEvent
{
    public CreatedEvent(T entity)
    {
        Entity = entity;
    }

    public T Entity { get; }
}
