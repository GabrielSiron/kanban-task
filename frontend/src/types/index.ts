export type Filter = {
    attr: string;
    operation: string;
    value: string;
}

export type RequestParams = {
    filters: Array<Filter> | undefined;
    order_by: string | undefined;
} | undefined;

export type RequestBody = object;

export type Pagination = {
    current: number;
    next: number | null;
    previous: number | null;
    has_next: boolean;
    has_previous: boolean;
}

export type GetListResponse = {
    pagination: Pagination;
    data: Array<any>;
}

export type GetDetailsResponse = {
    data: object;
}